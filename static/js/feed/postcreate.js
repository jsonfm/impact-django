const image = document.getElementById("image");
const imageInput = document.getElementById("imageInput");


const loadImage = (e) => {

    if(!e.target.files.length) return;

    const selectedFile = e.target.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', (e) => {
        image.title = selectedFile.name;
        image.src = e.target.result;
    });

    reader.readAsDataURL(selectedFile);
}

window.addEventListener('load', () => {
    imageInput.addEventListener("change", loadImage);
});