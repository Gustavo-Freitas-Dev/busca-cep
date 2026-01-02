function copiarEndereco() {
    const texto = document.getElementById("result-list").innerText;
    const icon = document.querySelector(".copy-btn i");

    navigator.clipboard.writeText(texto).then(() => {
        icon.classList.remove("fa-copy");
        icon.classList.add("fa-check");

        setTimeout(() => {
            icon.classList.remove("fa-check");
            icon.classList.add("fa-copy");
        }, 1500);
    });
}
