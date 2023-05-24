let API_KEY_GOOGLE = 'AIzaSyAYSeZRkkIEUkvEc1Ut7UYs7q0lLRZds94';
let API_KEY_WEATHER = 'ea0fd615af4fb560a1416a516e50b782';

let map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 35.7804643, lng: 139.7151025 },
    zoom: 15
  });
}

function apiError(error) {
  console.log('ERROR: ' + error);
}


function findWeather() {
  let inputAddress = document.getElementById('input-address');
  let address = inputAddress.value;

  fetch('https://maps.googleapis.com/maps/api/geocode/json?address=' + encodeURI(address) + '&key=' + API_KEY_GOOGLE)
  .then(response => response.json())
  .then(displayCoordinate)
  .catch(apiError);
}

function displayCoordinate(result) {

  if (result == null) {
    return;
  }
  let location = result.results[0].geometry.location;
  let lat = document.getElementById('latitude');
  let lon = document.getElementById('longitude');
  lat.textContent = location.lat;
  lon.textContent = location.lng;

  let x_lat = location.lat;
  let y_lon = location.lng;
 
  fetch('http://api.openweathermap.org/data/2.5/weather?lat=' + x_lat + '&lon=' + y_lon + '&appid=' + API_KEY_WEATHER)
  .then(response => response.json())
  .then(displayWeather)
  .catch(apiError)


  let inputLatitude2 = location.lat;
  let inputLongitude2 = location.lng;
  map.setCenter({ lat: Number(inputLatitude2), lng: Number(inputLongitude2) });


 
  // 2. 緯度経度を表示する

  // 3. OpenWeatherMapを利用して、その緯度経度の天気を取得する
  // 天気が取得できたら、displayWeatherが呼ばれるようにする

  // 4. 地図の中心を移動する

}

function displayWeather(result) {

  let city = document.getElementById('city');
  let weather = document.getElementById('td-weather');
  let temperature = document.getElementById('td-temperature');
  let humidity = document.getElementById('td-humidity');
  let pressure = document.getElementById('td-pressure');
  
  city.textContent = result.name;
  weather.textContent = result.weather[0].main;
  temperature.textContent = result.main.temp;
  humidity.textContent = result.main.humidity;
  pressure.textContent = result.main.pressure;

  // 5. 天気を表示する
  
}



