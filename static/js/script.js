$(document).ready(function () {
  let baseURL = $(location).attr("origin");
  //   console.log(baseURL + "/");
  $(".baseUrl").text(baseURL + "/");

  // copying function
  function copyToClipboard(element) {
    try {
      if (navigator.clipboard) {
        navigator.clipboard.writeText(element.text());
        alert("Link copied to clipboard!");
      } else {
        throw "Your browser doesn't support text copy.";
      }
    } catch (err) {
      console.error("Error!", err);
      var $temp = $("<input/>");
      $("body").append($temp);
      $temp.val($(element).text()).select();
      document.execCommand("copy");
      alert("Link copied to clipboard!");
      $temp.remove();
    }
  }

  $("#copy-btn").click(function (e) {
    e.preventDefault();
    copyToClipboard($("#short-url"));
  });
});
