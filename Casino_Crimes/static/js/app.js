// // Use D3 fetch to read the JSON file
// The data from the JSON file is arbitrarily named importedData as the argument
d3.json("/SuspiciousActivity").then(function (importedData) {
  // console.log(importedData);
  var data = importedData;
  //   // Sort the data array using the Count value
  var sortedData = data.sort(function (a, b) {
    return parseFloat(b.Count) - parseFloat(a.Count);
  });
  //   // Slice the first 10 objects for plotting
  sliceData = sortedData.slice(0,10);
  //   // Reverse the array due to Plotly's defaults
  reverseData = sliceData.reverse();
  //   // Trace1 for the SuspiciousActivity Data
  var trace1 = {
    x: reverseData.map((row) => row.Count),
    y: reverseData.map((row) => row.SuspiciousActivity),
    text: reverseData.map((row) => row.State),
    name: "Industry",
    type: "bar",
    orientation: "h"
  };
  // var trace2 = {
  //   x: data.map(row => row.Industry),
  //   y: data.map(row => row.Count),
  //   text: data.map(row => row.State),
  //   name: "SuspiciousActivIndustryity",
  //   type: "bar",
  //   // orientation: "h"
  // };

  //   // data
  var chartData = [trace1];
  //   // Apply the group bar mode to the layout
  var layout = {
    title: "Top Suspicious activities",
    // barmode: 'stack',
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100,
    },
  };
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plotly", chartData, layout);
});

// function buildPlot() {
  const url = "/industry";

  d3.json(url).then(function (importedData) {
    // console.log(importedData);
    var data = importedData;
    // console.log(data);

    var az = data.filter((d) => d.State === "Arizona");
    var ca = data.filter((d) => d.State === "California");
    var co = data.filter((d) => d.State === "Colorado");
    var nv = data.filter((d) => d.State === "Nevada");
    var nm = data.filter((d) => d.State === "New Mexico");
    var ut = data.filter((d) => d.State === "Utah");
    // console.log(az);

    // });

    // var states = [az,ca,co,nv,nm,ut];

    // for (i=0; i<states.length; i++) {
    //   var labels = states[i].map((s)=>s.Industry);
    //   var values = states[i].map((s)=>s.Count);
    //   console.log(labels);
    //   console.log(values);

    // Create an array of labels
    var labels = az.map((a) => a.Industry);
    var values = az.map((a) => a.Count);
  // });
// }
    // function init() {
      var data = [
        {
          type: "pie",
          values: values,
          labels: labels,
          // hovertext: states,
        },
      ];

      var layout = {
        showlegend: true,
      };
      Plotly.newPlot("pie", data, layout);
    
  })
  //   buildPlot()
  // };
    
  
  

//   // // On change to the DOM, call getData()
  d3.selectAll("#selDataset").on("change", getData);

  // Function called by DOM changes
  function getData() {
    var dropdownMenu = d3.select("#selDataset");
    // Assign the value of the dropdown menu option to a variable
    var dataset = dropdownMenu.property("value");
    console.log(dataset)
    // Initialize an empty array for the country's data
    var data = [];

    if (dataset == "az") {
      data = az;
    } else if (dataset == "ca") {
      data = ca;
    } else if (dataset == "co") {
      data = co;
    }
    if (dataset == "nv") {
      data = nv;
    } else if (dataset == "nm") {
      data = nm;
    } else if (dataset == "ut") {
      data = ut;
    }

    // Call function to update the chart
    updatePlotly(data);
  }

  // Update the restyled plot's values
  function updatePlotly(newdata) {
    Plotly.restyle("pie", "values", [newdata]);
  }


// init();
