
var map = L.map('map').setView([-12.099167, -77.034722], 14); // Andalucía

var osmLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap<\/a> contributors'
}).addTo(map);

function popUpInfo(feature, layer) {
    // does this feature have a property named popupContent?
    if (feature.properties && feature.properties.Direction) {
    	// "Speed": "50.00km/h"}
        layer.bindPopup(
        	"<p>\
        		<b>N°: </b>" + feature.properties['N'] + "<br/>\
        		<b>BaseStation ID: </b>" + feature.properties['BaseStation ID'] + "<br/>\
        		<b>Channel ID :</b>" + feature.properties['Channel ID'] + "<br/>\
        		<b>Device Name: </b>" + feature.properties['Device Name'] + "<br/>\
        		<b>Direction: </b>" + feature.properties['Direction'] + "<br/>\
        		<b>GPS Time: </b>" + feature.properties['GPS Time'] + "<br/>\
        		<b>Receiving Time: </b>" + feature.properties['Receiving Time'] + "<br/>\
        		<b>Speed: </b>" + feature.properties['Speed'] + "<br/>\
        		<b>Longitude: </b>" + feature.geometry['coordinates'][0] + "<br/>\
        		<b>Latitude: </b>" + feature.geometry['coordinates'][1] + "<br/>\
        	<p>"
        );
        //layer.bindPopup("<b>"+feature.properties.nomb_mus);
    }
}
L.geoJson(museos, {
    onEachFeature: popUpInfo
    }).addTo(map);


