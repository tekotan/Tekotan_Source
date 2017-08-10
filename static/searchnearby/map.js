function initMap() {
    function setMapOnAll(map) {
        for (var i = 0; i < marker_array.length; i++) {
            marker_array[i].setMap(map);
        }
    }

    // Removes the markers from the map, but keeps them in the array.
    function clearMarkers() {
        setMapOnAll(null);
    }
    //Deletes all markers in the array by removing references to them.
    function deleteMarkers() {
        clearMarkers();
        markers = [];
    }
    var types_choice = []
    var marker_array = []
    //alert(types_choice)
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -33.8688, lng: 151.2195 },
        zoom: 3
    });
    var infoWindow = new google.maps.InfoWindow({ map: map });
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            infoWindow.setPosition(pos);
            infoWindow.setContent('Location found.');
            map.setCenter(pos);
        }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }


    function callback(results, status) {
        if (status == google.maps.places.PlacesServiceStatus.OK) {
            for (var i = 0; i < results.length; i++) {
                createMarker(results[i]);

            }
            //alert(results)
        }
    }
    infowindow2 = new google.maps.InfoWindow({
        content: null
    })
    for (var i = 0; i < marker_array.length; i++) {

        var marker2 = marker_array[i];

        google.maps.event.addListener(marker2, 'click', function() {

            // where I have added .html to the marker object.

            infowindow.setContent('<p>hello</p>');
            infowindow.open(map, marker2);

        });

    }

    function getLatLng(query) {
 
    }
    var input1 = document.getElementById('pac-input').value
    //alert(getLatLng(input1))
    function createMarker(place) {
        var placeLoc = place.geometry.location;
        var marker1 = new google.maps.Marker({
            map: map,
            position: place.geometry.location
        });
        marker_array.push(marker1)
    }
    var input = /** @type {!HTMLInputElement} */(
        document.getElementById('pac-input'));
    //alert("shdjfhdsjkfh")


    //alert("fsdfsdf")


    var types = document.getElementById('type-selector');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(types);

    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);

    var infowindow1 = new google.maps.InfoWindow();
    var marker = new google.maps.Marker({
        map: map,
        anchorPoint: new google.maps.Point(0, -29)
    });
    marker_array.push(marker)

    autocomplete.addListener('place_changed', function() {
        infowindow1.close();
        marker.setVisible(false);
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert("Autocomplete's returned place contains no geometry");
            return;
        }

        // If the place has a geometry, then present it on a map.
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);  // Why 17? Because it looks good.
        }
        marker.setIcon(/** @type {google.maps.Icon} */({
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(35, 35)
        }));
        var typeee = ['restaurant', 'school']
        //alert(place.geometry.location)
        marker.setPosition(place.geometry.location);
        marker.setVisible(true);
        if (document.getElementById('choices').value == 'health') {
            types_choice = ['health']
        } else if (document.getElementById('choices').value == 'food') {
            types_choice = ['food']
        } else if (document.getElementById('choices').value == 'place_of_worship') {
            types_choice = ['place_of_worship']
        } else if (document.getElementById('choices').value == 'museum') {
            types_choice = ['museum']
        } else if (document.getElementById('choices').value == 'bank') {
            types_choice = ['bank']
        } else if (document.getElementById('choices').value == 'library') {
            types_choice = ['library']
        } else if (document.getElementById('choices').value == 'pharmacy') {
            types_choice = ['pharmacy']
        } else if (document.getElementById('choices').value == 'gas_station') {
            types_choice = ['gas_station']
        } else if (document.getElementById('choices').value == 'grocery_or_supermarket') {
            types_choice = ['grocery_or_supermarket']
        } else if (document.getElementById('choices').value == 'school') {
            types_choice = ['school']
        } else if (document.getElementById('choices').value == 'department_store') {
            types_choice = ['department_store']
        } else if (document.getElementById('choices').value == 'convenience_store') {
            types_choice = ['convenience_store']
        } else if (document.getElementById('choices').value == 'local_government_office') {
            types_choice = ['local_government_office']
        } else if (document.getElementById('choices').value == 'restaurant') {
            types_choice = ['restaurant']
        }
        //alert(types_choice)
        var request = {
            location: /*getLatLng(input1)*/place.geometry.location,
            radius: 1000,
            types: types_choice // this is where you set the map to get the hospitals and health related places
        };
        //alert("hdfsijhfj")
        infowindow = new google.maps.InfoWindow();
        clearMarkers();
        var service = new google.maps.places.PlacesService(map);
        service.nearbySearch(request, callback);
        var address = '';
        if (place.address_components) {
            address = [
                (place.address_components[0] && place.address_components[0].short_name || ''),
                (place.address_components[1] && place.address_components[1].short_name || ''),
                (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
        }

        infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
        infowindow.open(map, marker);
    });

    // Sets a listener on a radio button to change the filter type on Places
    // Autocomplete.
    autocomplete.setTypes([]);
}