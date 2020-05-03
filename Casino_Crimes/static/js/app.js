  function buildPlot(casino) {
    const url = "/Industry";

    d3.json(url).then(function (data) {
      console.log(data);

      var states = data.State;
      var industry = data.Industry;
      var lat = data.Lat;
      var long = data.long;
      var count = data.Count;

      var az = data.filter(d => d.State ==="Arizona");
      var ca = data.filter(d => d.State ==="California");
      var co = data.filter(d => d.State ==="Colorado");
      var nv = data.filter(d => d.State ==="Nevada");
      var nm = data.filter(d => d.State ==="New Mexico");
      var ut = data.filter(d => d.State ==="Utah");

    });
  }

      // Create an array of music provider labels
  var casinos = data.Count(az);
  
  

  function init() {
      var data = [
        {
          type: "pie",
          values: az,
          labels: casinos,
          // hovertext: states,
        },
      ];

      var layout = {
        showlegend: true,
      };
      Plotly.newPlot("pie", data, layout);
    };
  

// // On change to the DOM, call getData()
  d3.selectAll("#selDataset").on("change", getData);

// Function called by DOM changes
    function getData() {
    var dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
    var dataset = dropdownMenu.property("value");
  // Initialize an empty array for the country's data
    var data = [];

    if (dataset == 'az') {
      data = az;
    }
    else if (dataset == 'ca') {
      data = ca;
    }
    else if (dataset == 'co') {
      data = co;
    }
    if (dataset == 'nv') {
      data = nv;
    }
    else if (dataset == 'nm') {
      data = nm;
    }
    else if (dataset == 'ut') {
      data = ut;
    }




  // Call function to update the chart
    updatePlotly(data);
    }

// Update the restyled plot's values
function updatePlotly(newdata) {
  Plotly.restyle("pie", "values", [newdata]);
  }

init();
