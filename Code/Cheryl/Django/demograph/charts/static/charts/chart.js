// scatter and line plots. Change out "mode" for "lines" or "markers"
//change out 'type' for 'scatter' (line and scatter plots), 'bar' (bar graphs)
// can either have plotly menu bar always on, hidden until mouseover, or completely hidden. See bottom of page for other options
test = 'scatter'
trace1 = {
  type: 'scatter',
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  mode: 'lines',
  name: 'Red',
  line: {
    color: 'rgb(219, 64, 82)',
    width: 3
  }
};

trace2 = {
  type: test,
    // type: 'bar',
  x: [1, 2, 3, 4],
  y: [12, 9, 15, 12],
  mode: 'markers',
  name: 'Blue',
  line: {
    color: 'rgb(55, 128, 191)',
    width: 1
  }
};

var data = [trace1, trace2];

var layout = {
    title: 'Hide the Modebar',
    showlegend: true
};

Plotly.newPlot('finalGraph', data, layout, {displayModeBar: false});





// to make it editable with plotly on their site, always shows
// var layout = {
//     title: 'Always Display the Modebar',
//     showlegend: false};
// Plotly.newPlot('myDiv', data, layout, {displayModeBar: true});