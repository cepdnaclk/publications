function addBookmark(title, url) {
// TODO: Implement a better solution 

  // if (window.sidebar && window.sidebar.addPanel) { // Firefox
  //   window.sidebar.addPanel(title, url, '');
  // } else if (window.external && ('AddFavorite' in window.external)) { // IE
  //   window.external.AddFavorite(url, title);
  // } else if (window.opera && window.print) { // Opera
  //   var elem = document.createElement('a');
  //   elem.setAttribute('href',url);
  //   elem.setAttribute('title',title);
  //   elem.setAttribute('rel','sidebar');
  //   elem.click();
  // } else { // Other browsers (mainly WebKit - Chrome/Safari)
  //   alert('Press ' + (navigator.userAgent.toLowerCase().indexOf('mac') != -1 ? 'Command/Cmd' : 'CTRL') + '+D to bookmark this page.');
  // }
  window.location.hash = url

  $('#toast-message').html('Press ' + (navigator.userAgent.toLowerCase().indexOf('mac') != -1 ? 'Command/Cmd' : 'CTRL') + '+D to bookmark this page.')
  $('#liveToast').show()
  setTimeout(function() { 
        $('#liveToast').hide()
  }, 4000);

}


$(document).ready(()=>{
  $('#liveToast').addClass('showing').hide()
});