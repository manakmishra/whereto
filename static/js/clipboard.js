function copyToClipboard() {
    var element = document.getElementById("short_url");
    element.select();
    element.setSelectionRange(0, 99999);
    
    navigator.clipboard.writeText(element.value).then(function() {
      //Successfullt copied
    }, function() {
      //fallback using deprecated execCommand API
      document.execCommand("copy");
    });

    alert("Copied to Clipboard!");
}