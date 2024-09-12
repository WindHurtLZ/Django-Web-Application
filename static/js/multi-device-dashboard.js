const initializeDeviceCharts = () => {
  const devices = document.querySelectorAll('[data-device-chart]');

  devices.forEach((device, index) => {
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

      // 平滑车速波动函数
      const generateSpeed = (prevValue) => {
          const delta = (Math.random() - 0.5) * 10;  // 让车速在前值的基础上上下浮动（-10到+10）
          let newValue = prevValue + delta;
          if (newValue > 120) newValue = 120;  // 保证车速不超过 120
          if (newValue < 0) newValue = 0;  // 保证车速不低于 0
          return newValue;
      };

      // Fake real-time data
      let data = [];  // 初始化一个空数组来存储平滑车速数据
      let initialSpeed = Math.random() * 120;  // 设置第一个初始车速值
      for (let i = 0; i < 50; i++) {
          initialSpeed = generateSpeed(initialSpeed);  // 使用平滑函数生成后续车速
          data.push(initialSpeed);  // 将生成的车速数据添加到数组中
      }

      // Fake real-time labels
      const generateDates = () => {
          const now = new Date();
          const dates = [];
          data.forEach((v, i) => {
              dates.push(new Date(now - 2000 - i * 2000));
          });
          return dates;
      };
      const labels = generateDates();
      let range = 35;
      let increment = 0;
      const slicedData = data.slice(0, range);
      const slicedLabels = labels.slice(0, range).reverse();

      const chart = new Chart(ctx, {
          type: 'line',
          data: {
              labels: slicedLabels,
              datasets: [
                  // Indigo line
                  {
                      data: slicedData,
                      fill: true,
                      backgroundColor: `rgba(${hexToRGB('#3b82f6')}, 0.08)`,
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
                  },
              ],
          },
          options: {
              layout: {
                  padding: 20,
              },
              scales: {
                  y: {
                      border: {
                          display: false,
                      },
                      suggestedMin: 30,
                      suggestedMax: 80,
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
                          parser: 'hh:mm:ss',
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

      // Fake real-time updates
      const chartValue = device.querySelector('[data-device-value]');
      const chartDeviation = device.querySelector('[data-device-deviation]');

      const adddata = (prev) => {
          const newValue = generateSpeed(prev);  // 生成平滑波动的新车速
          const {datasets} = chart.data;
          chart.data.labels.shift();
          chart.data.labels.push(new Date());
          datasets[0].data.shift();
          datasets[0].data.push(newValue);
          chart.update(0);

          if (!chartValue) return;
          const diff = ((newValue - prev) / prev) * 100;
          chartValue.innerHTML = newValue.toFixed(2);
          if (!chartDeviation) return;
          chartDeviation.style.backgroundColor = diff < 0 ? '#f59e0b' : '#10b981';
          chartDeviation.innerHTML = `${diff > 0 ? '+' : ''}${diff.toFixed(2)}%`;
          return newValue;
      };

      let currentSpeed = data[0];  // initial current speed
      const reload = () => {
          currentSpeed = adddata(currentSpeed);  // use latest data to generate next
          setTimeout(reload, 2000);  // update every 2s
      };
      reload();

      document.addEventListener('darkMode', (e) => {
          const {mode} = e.detail;
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
  });
};
// Call the function to initialize all device charts
initializeDeviceCharts();