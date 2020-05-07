// Create a map object
var myMap = L.map("map", {
  center: [33.31, -114.7],
  zoom: 5,
});
var street = L.tileLayer(
  "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}",
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: "mapbox.streets-basic",
    accessToken: API_KEY,
  }
).addTo(myMap);
function getData() {
  d3.json("/county").then( function (data) {
    data.forEach(function (d) {
      var lat = d.Lat;``
      var long = d.Long;
      var name = d.State;
      var industry = d.Industry;
      var place = {
        latitude: lat,
        longitude: long,
        name: name,
        industry: industry,
      };
      var color;
      switch (place.industry) {
        case " State Licensed Casino":
          color = "blue";
          break;
        case " Card Club":
          color = "red";
          break;
        // case 'W':
        //     color = 'white';
        //     break;
        // case 'K': // as in kobolt
        //     color = 'black';
        //     break;
        default:
          color = "green";
          break;
      }
      var circle = L.circle([place.latitude, place.longitude], {
        color: color,
        fillOpacity: 0.5,
        radius: 12000,
      }).addTo(myMap);
      circle.bindPopup(place.industry).openPopup();
      //  mydata.push(dictO);
    });
  });
};
getData();