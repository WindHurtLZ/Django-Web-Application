const initializeDeviceCharts = () => {
    const devices = document.querySelectorAll('[data-device-chart]');

    devices.forEach((device) => {
        const ctx = device.querySelector('canvas').getContext('2d');
        const deviceId = device.dataset.deviceId;

        if (!ctx) return;

        const darkMode = localStorage.getItem('dark-mode') === 'true';

        const textColor = {
            light: '#94a3b8',
            dark: '#64748B'
        };

        const gridColor = {
            light: '#f1f5f9',
            dark: '#334155'
        };

        const tooltipTitleColor = {
            light: '#1e293b',
            dark: '#f1f5f9'
        };

        const tooltipBodyColor = {
            light: '#1e293b',
            dark: '#f1f5f9'
        };

        const tooltipBgColor = {
            light: '#ffffff',
            dark: '#334155'
        };

        const tooltipBorderColor = {
            light: '#e2e8f0',
            dark: '#475569'
        };

        // get real data
        fetch(`/device_speed_data/${deviceId}/`)
            .then(response => response.json())
            .then(result => {
                if (result.status === 'success') {
                    const dataPoints = result.data;
                    const data = dataPoints.map(dp => dp.speed);
                    const labels = dataPoints.map(dp => new Date(dp.timestamp));

                    // last timestamp
                    let lastTimestamp = labels[labels.length - 1];

                    const chart = new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: labels,
                            datasets: [
                                {
                                    data: data,
                                    fill: true,
                                    backgroundColor: `rgba(${hexToRGB('#3b82f6')}, 0.05)`,
                                    borderColor: '#6366f1',
                                    borderWidth: 2,
                                    tension: 0,
                                    pointRadius: 0,
                                    pointHoverRadius: 3,
                                    pointBackgroundColor: '#6366f1',
                                    pointHoverBackgroundColor: '#6366f1',
                                    pointBorderWidth: 0,
                                    pointHoverBorderWidth: 0,
                                    clip: 20,
                                    spanGaps: false,
                                },
                            ],
                        },
                        options: {
                            layout: {
                                padding: {
                                    left: 10,
                                    right: 10,
                                    bottom: 0,
                                }
                            },
                            scales: {
                                y: {
                                    border: {
                                        display: false,
                                    },
                                    suggestedMin: 0,
                                    suggestedMax: 120,
                                    ticks: {
                                        maxTicksLimit: 5,
                                        callback: (value) => formatValue(value),
                                        color: darkMode ? textColor.dark : textColor.light,
                                    },
                                    grid: {
                                        color: darkMode ? gridColor.dark : gridColor.light,
                                    },
                                },
                                x: {
                                    type: 'time',
                                    time: {
                                        parser: 'HH:mm:ss',
                                        unit: 'second',
                                        tooltipFormat: 'MMM DD, H:mm:ss a',
                                        displayFormats: {
                                            second: 'H:mm:ss',
                                        },
                                    },
                                    border: {
                                        display: false,
                                    },
                                    grid: {
                                        display: false,
                                    },
                                    ticks: {
                                        autoSkipPadding: 48,
                                        maxRotation: 0,
                                        color: darkMode ? textColor.dark : textColor.light,
                                    },
                                },
                            },
                            plugins: {
                                legend: {
                                    display: false,
                                },
                                tooltip: {
                                    titleFont: {
                                        weight: '600',
                                    },
                                    callbacks: {
                                        label: (context) => formatValue(context.parsed.y),
                                    },
                                    titleColor: darkMode ? tooltipTitleColor.dark : tooltipTitleColor.light,
                                    bodyColor: darkMode ? tooltipBodyColor.dark : tooltipBodyColor.light,
                                    backgroundColor: darkMode ? tooltipBgColor.dark : tooltipBgColor.light,
                                    borderColor: darkMode ? tooltipBorderColor.dark : tooltipBorderColor.light,
                                },
                            },
                            interaction: {
                                intersect: false,
                                mode: 'nearest',
                            },
                            animation: false,
                            maintainAspectRatio: false,
                        },
                    });

                    // update real time
                    const chartValue = device.querySelector('[data-device-value]');
                    const chartDeviation = device.querySelector('[data-device-deviation]');

                    const updateChart = () => {
                        fetch(`/device_latest_speed/${deviceId}/?since=${encodeURIComponent(lastTimestamp.toISOString())}`)
                            .then(response => response.json())
                            .then(result => {
                                console.log('Result status:', result.status);
                                if (result.status === 'success') {
                                    const latestData = result.data;
                                    const newTimestamp = new Date(latestData.timestamp);
                                    console.log(`lastTimestamp: ${lastTimestamp.toISOString()}, newTimestamp: ${newTimestamp.toISOString()}`);

                                    if (newTimestamp > lastTimestamp) {
                                        const newValue = latestData.speed;

                                        chart.data.labels.push(newTimestamp);
                                        chart.data.datasets[0].data.push(newValue);

                                        if (chart.data.labels.length > 10) {
                                            chart.data.labels.shift();
                                            chart.data.datasets[0].data.shift();
                                        }

                                        chart.update('none');

                                        lastTimestamp = newTimestamp;

                                        if (chartValue) {
                                            chartValue.innerHTML = newValue.toFixed(2);
                                        }

                                        if (chartDeviation) {
                                            chartDeviation.style.backgroundColor = newValue > 40 ? (newValue > 80 ? '#ff3d00' : '#f59e0b') : '#10b981';
                                            chartDeviation.innerHTML = newValue > 40 ? (newValue > 80 ? 'Over Speed' : 'Danger') : 'Safe';
                                        }
                                    } else {
                                        console.warn('Received data is not newer than last timestamp.');
                                    }
                                } else if (result.status === 'no_new_data') {

                                    console.log('No new data received.');
                                } else {
                                    console.error('Unexpected status:', result.status);
                                }

                                setTimeout(updateChart, 2000);
                            })
                            .catch(error => {
                                console.error('Error fetching latest speed data:', error);
                                setTimeout(updateChart, 2000);
                            });
                    };

                    updateChart();

                    document.addEventListener('darkMode', (e) => {
                        const { mode } = e.detail;
                        if (mode === 'on') {
                            chart.options.scales.x.ticks.color = textColor.dark;
                            chart.options.scales.y.ticks.color = textColor.dark;
                            chart.options.scales.y.grid.color = gridColor.dark;
                            chart.options.plugins.tooltip.titleColor = tooltipTitleColor.dark;
                            chart.options.plugins.tooltip.bodyColor = tooltipBodyColor.dark;
                            chart.options.plugins.tooltip.backgroundColor = tooltipBgColor.dark;
                            chart.options.plugins.tooltip.borderColor = tooltipBorderColor.dark;
                        } else {
                            chart.options.scales.x.ticks.color = textColor.light;
                            chart.options.scales.y.ticks.color = textColor.light;
                            chart.options.scales.y.grid.color = gridColor.light;
                            chart.options.plugins.tooltip.titleColor = tooltipTitleColor.light;
                            chart.options.plugins.tooltip.bodyColor = tooltipBodyColor.light;
                            chart.options.plugins.tooltip.backgroundColor = tooltipBgColor.light;
                            chart.options.plugins.tooltip.borderColor = tooltipBorderColor.light;
                        }
                        chart.update('none');
                    });
                } else {
                    console.error('Failed to fetch initial data:', result.message);
                }
            })
            .catch(error => {
                console.error('Error fetching speed data:', error);
            });
    });
};

initializeDeviceCharts();
