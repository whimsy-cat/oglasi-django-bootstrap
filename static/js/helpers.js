function resetQueryParams() {
  const urlParams = new URLSearchParams(window.location.search);
  const prikaz = urlParams.get('prikaz');

  if (location.href.includes('?')) { 
    window.history.pushState({}, document.title, window.location.pathname);
  }

  if (prikaz) {
    document.location.search = 'prikaz=' + prikaz;
  } else {
    location.reload()
  }
}
/**
 * Adding URL Query Params based on key and value for listings:
 * - sort params
 * - page param
 * - filters params
 * - page view param
 * @param {string} key 
 * @param {string} value 
 */

function queryParam(key, value) {
    key = encodeURIComponent(key);
    value = encodeURIComponent(value);

    var kvp = document.location.search.substr(1).split('&');
    let i=0;

    for(; i<kvp.length; i++){
        if (kvp[i].startsWith(key + '=')) {
            let pair = kvp[i].split('=');
            pair[1] = value;
            kvp[i] = pair.join('=');
            break;
        }
    }

    if(i >= kvp.length){
        kvp[kvp.length] = [key,value].join('=');
    }
    // To do: Find other solution
    // If filter cena remove max-min price
    if (kvp && key === 'cena') {
      kvp = kvp.filter(k => !k.includes('max-price='))
      kvp = kvp.filter(k => !k.includes('min-price='))
    }
    if (kvp && key === 'povrsina') {
      kvp = kvp.filter(k => !k.includes('max-size='))
      kvp = kvp.filter(k => !k.includes('min-size='))
    }
    if (kvp && key === 'spratnost') {
      kvp = kvp.filter(k => !k.includes('max-spratnost='))
      kvp = kvp.filter(k => !k.includes('min-spratnost='))
    }

    // Reseting pagination when sort / filter changed
    // but keep page if we are switching it
    if (kvp && key !== 'page') {
      kvp = kvp.filter(k => !k.includes('page='))
    }

    // When view changed remove all filters
    if (kvp && key === 'prikaz') {
      kvp = kvp.filter(k => k.includes('prikaz='))
    }

    let params = kvp.join('&')

    document.location.search = params;
  }
