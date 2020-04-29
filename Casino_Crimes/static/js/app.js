
const url = "/api/casinos";
//d3.json(url).then(function(response) {

//     console.log(response);

//     const data = response;


// var tableData = data;
// YOUR CODE HERE!
const tbody = d3.select("tbody");
function buildTable(casinos) {
  tbody.html("");
  // const url = "/api/casinos";

  d3.json(url).then(function(response) {

    console.log(response);

    const data = response;

  casinos.forEach(dataRow => {
    const row = tbody.append("tr");
    Object.values(dataRow).forEach(val => {
      let cell = row.append("td");
      cell.text(val);
    });
  });
});
// }

// function setup(){
//   loadJSON(url, gotData,jsonp);
// }
// function gotData(data){
//   console.log(data)
// }