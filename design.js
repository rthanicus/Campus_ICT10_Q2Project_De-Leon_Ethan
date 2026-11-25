// Glitch effect on the ARASAKA logo every few seconds
var logo = document.getElementById("logo");

function glitchLogo() {
    logo.classList.add("glitch");

    // remove the glitch after a very short time
    setTimeout(function () {
        logo.classList.remove("glitch");
    }, 150);
}

setInterval(glitchLogo, 3000);

// Red light that follows the mouse
var glow = document.createElement("div");
glow.className = "mouse-glow";
document.body.appendChild(glow);

document.addEventListener("mousemove", function (event) {
    glow.style.left = event.clientX + "px";
    glow.style.top = event.clientY + "px";
});

