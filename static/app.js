//let form = document.querySelector('#myForm')
//let name = document.querySelector('.location')
//
//document.addEventListener('DOMContentLoaded', function() {
//    form.addEventListener('submit', function(e) {
//    e.preventDefault();
//    name.value;
//    let data = { 'name': name };
//
//    let xhr = new XMLHttpRequest();
//    xhr.open('GET', '/', true);
//    xhr.setRequestHeader('Content-Type', 'application/json');
//    xhr.onreadystatechange = function() {
//      if (xhr.readyState === XMLHttpRequest.DONE) {
//        if (xhr.status === 200) {
//          let response = JSON.parse(xhr.responseText);
//          console.log(response);
//          // Handle the response here
//        } else {
//          console.log('Error:', xhr.status);
//          // Handle the error here
//        }
//      }
//    };
//    xhr.send(JSON.stringify(data));
//  });
//});
