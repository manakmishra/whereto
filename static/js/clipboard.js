function myFunction() {
    var copyText = document.getElementById("short_url");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
    alert("Copied the URL: " + copyText.value);
  }