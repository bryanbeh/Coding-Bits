function initMap() {

  var bounds = new google.maps.LatLngBounds;
  var markersArray = [];

  var origin = 'Self';
  var destinationA = 'Cannon Street Station, London';
  var destinationB = "IDEA, London";
  var destinationC = "Liverpool Street, London";
  var destinationD = "Moorgate, London";
  var destinationE = "Duck & Waffle, London";
  var destinationF = "Bank of England, London";
  var destinationG = "Tower of London, London";

  var destinationIcon = 'https://chart.googleapis.com/chart?' +
      'chst=d_map_pin_letter&chld=D|FF0000|000000';
  var originIcon = 'https://chart.googleapis.com/chart?' +
      'chst=d_map_pin_letter&chld=O|FFFF00|000000';
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 51.4947, lng: -0.1732},
    zoom: 15
  });
  var infoWindow = new google.maps.InfoWindow;
  var geocoder = new google.maps.Geocoder;

  var service = new google.maps.DistanceMatrixService;
  var q = prompt('Give me a radius for your restaurants:')

  if(q < 4){
    return
  }
  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      infoWindow.setPosition(pos);
      infoWindow.setContent('Location found.');
      infoWindow.open(map);
      map.setCenter(pos);

      service.getDistanceMatrix({
        origins: [pos],
        destinations: [destinationA, destinationB, destinationC, destinationD, destinationE, destinationF, destinationG],
        travelMode: 'WALKING',
        unitSystem: google.maps.UnitSystem.METRIC,
        avoidHighways: false,
        avoidTolls: false
      }, function(response, status) {
        if (status !== 'OK') {
          alert('Error was: ' + status);
        } else {
          var originList = response.originAddresses; //maybe can remove
          var destinationList = response.destinationAddresses;
          var outputDiv = document.getElementById('output');
          outputDiv.innerHTML = '';
          deleteMarkers(markersArray);

          var showGeocodedAddressOnMap = function(asDestination) {
            var icon = asDestination ? destinationIcon : originIcon;
            return function(results, status) {
              if (status === 'OK') {
                map.fitBounds(bounds.extend(results[0].geometry.location));
                markersArray.push(new google.maps.Marker({
                  map: map,
                  position: results[0].geometry.location,
                  icon: icon
                }));
              } else {
                alert('Geocode was not successful due to: ' + status);
              }
            };
          };

          for (var i = 0; i < originList.length; i++) {
            var results = response.rows[i].elements;
            geocoder.geocode({'address': originList[i]},
                showGeocodedAddressOnMap(false));
            for (var j = 0; j < results.length; j++) {
              if(parseInt(results[j].duration.text.slice(0,2)) < q){
                geocoder.geocode({'address': destinationList[j]},
                    showGeocodedAddressOnMap(true));
                outputDiv.innerHTML += originList[i] + ' to ' + destinationList[j] +
                    ': ' + results[j].distance.text + ' in ' +
                    results[j].duration.text + '<br>';
                    console.log(results[j].duration.text.slice(0,2))
              }
            }
          }
        }
      });

    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
}

function deleteMarkers(markersArray) {
  for (var i = 0; i < markersArray.length; i++) {
    markersArray[i].setMap(null);
  }
  markersArray = [];
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}
