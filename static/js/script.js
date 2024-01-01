var loadFile_music = function(event){
    var file_name = document.getElementById('output-music');
    console.log();
    file_name.textContent = event.target.files[0].name;
    var input_music = document.getElementById('label-music');
    input_music.textContent = "Almashtirish";
    input_music.classList.add('selected');
  };
var loadFile_txt = function(event) {
    var name = document.getElementById('output-txt');
    console.log();
    name.textContent = event.target.files[0].name;
    var input_txt = document.getElementById('label-txt');
    input_txt.textContent = "Almashtirish";
    input_txt.classList.add('selected');
  };
var loadFile_img = function(event) {
    var image = document.getElementById('output-img');
    console.log();
    image.src = URL.createObjectURL(event.target.files[0]);
    var input_img = document.getElementById('label-img');
    input_img.textContent = "Almashtirish";
    input_img.classList.add('selected');
  };

