const GEOCODER_URL = 'http://search.maps.sputnik.ru/search/addr?q=';

async function getData(address) {
    if (address !== '') {
        let query = GEOCODER_URL + address,
            response = await fetch(query);
        response = await response.json();
        if ('address' in response['result']) {
            return response;
        }
    }
}

async function getListAddress(request) {
    let response = await getData(request);
    if (response) {
        let dataAddress = response['result']['address'],
            addressList = [];
        for (let address of dataAddress) {
            if (address['features']) {
                for (let features of address['features']) {
                    addressList.push(features['properties']['display_name'])
                }
            }
        }
        return addressList
    }
}

async function mappingAddress(request) {
    let response = await getData(request);
    if (response) {

        let firstAddress = response['result']['address'][0]['features'][0],
            region = $('#id_region').val(''),
            place = $('#id_place').val(''),
            street = $('#id_street').val(''),
            house = $('#id_house').val('');
    
        for (let addressComponent of firstAddress['properties']['address_components']){
            switch(addressComponent['type']){
                case 'region':
                   region.val(addressComponent['value']);
                    break;
                case 'place':
                    place.val(addressComponent['value']);
                    break;
                case 'street':
                    let value = addressComponent['value'].replace('улица ', ''); 
                    street.val(value);
                    break;
            }
        }

        let displayName = firstAddress['properties']['display_name'].split(',');
        let houseNum = +displayName.pop();
        house.val(houseNum ? houseNum: '');
        return firstAddress['geometry']['geometries'][0]['coordinates'];
    }
}