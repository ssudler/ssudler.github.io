const ctx = document.getElementById('test-chart').getContext('2d');
const myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Skin Tone 1', 'Skin Tone 2', 'Skin Tone 3', 'Skin Tone 4', 'Skin Tone 5', 'Skin Tone 6', 'Skin Tone 7', 'Skin Tone 8', 'Skin Tone 9', 'Skin Tone 10'],
    datasets: [{
      label: 'Color Trends in Basketball',
      data: [7, 8, 6, 5, 3.5, 2, 1.75, 1.5, 1.6, 1],
      backgroundColor: [
        'rgba(241, 230, 218, 1)',
        'rgba(220, 192, 163, 1)',
        'rgba(199, 155, 107, 1)',
        'rgba(198, 140, 83, 1)',
        'rgba(111, 79, 42, 1)',
        'rgba(55, 40, 21, 1)',
        'rgba(37, 27, 14, 1)',
        'rgba(37, 27, 14, 1)',
        'rgba(37, 27, 14, 1)',
        'rgba(37, 27, 14, 1)',
      ],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});