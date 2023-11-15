function loginToGenerate() {

    $("#searchbar").submit(function (e) {

        const value = document.getElementById("exampleInputPassword1").value;

        if (value == "t96HjklmZ") {

            window.location.href = "code.html";

            return false;
        }

    });

}

function openScanner()
{
    eel.open_scanner()();
}