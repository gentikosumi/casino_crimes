// Create a map object
var myMap = L.map("map", {
  center: [33.31, -114.70],
  zoom: 4
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: API_KEY
}).addTo(myMap);

var csvData;

console.log('Hi!');


d3.csv('./data/SARStats_6.csv', data => {
  csvData = data.splice(0,6);

  var row = d3.select('tbody').append('tr')

  csvData.forEach(obj => {
    var cell = row.append('td');

    console.log(obj);
    

    Object.values(obj).forEach(val => {
      cell.text(val);
    })
  });

})


// Count: "17"
// Countym: "Maricopa County, AZ"
// Industry: "Casino/Card Club - Tribal Authorized Casino"
// State: "Arizona"
// Year Month: "2014 January"