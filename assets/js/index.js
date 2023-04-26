function addBookmark(title, url) {
  if (window.sidebar && window.sidebar.addPanel) { // Firefox
    window.sidebar.addPanel(title, url, '');
  } else if (window.external && ('AddFavorite' in window.external)) { // IE
    window.external.AddFavorite(url, title);
  } else if (window.opera && window.print) { // Opera
    var elem = document.createElement('a');
    elem.setAttribute('href',url);
    elem.setAttribute('title',title);
    elem.setAttribute('rel','sidebar');
    elem.click();
  } else { // Other browsers (mainly WebKit - Chrome/Safari)
    alert('Press ' + (navigator.userAgent.toLowerCase().indexOf('mac') != -1 ? 'Command/Cmd' : 'CTRL') + '+D to bookmark this page.');
  }
  window.location.hash = url
}