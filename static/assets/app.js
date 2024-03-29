const validateEmail = function (email) {
  var formData = new FormData();
  formData.append("email", email);
  $.ajaxSetup({
    headers: {
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
  });
  $.ajax({
    url: "/validate/",
    type: "POST",
    dataType: "json",
    cache: false,
    processData: false,
    contentType: false,
    data: formData,
    error: function (xhr) {
      console.error(xhr.statusText);
    },
    success: function (res) {
      $(".error").text(res.msg);
    },
  });
};

const subscribeUser = function (email) {
  var formData = new FormData();
  formData.append("email", email);
  $.ajaxSetup({
    headers: {
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
  });
  $.ajax({
    url: "/newsletter/",
    type: "POST",
    dataType: "json",
    cache: false,
    processData: false,
    contentType: false,
    data: formData,
    error: function (xhr) {
      console.error(xhr.statusText);
    },
    success: function (res) {
      $(".success").text(res.msg);
      $("#userEmail").val(" ");
    },
  });
};

(function ($) {
  $("#submit").on("click", (event) => {
    event.preventDefault();
    const userEmail = $("#userEmail").val();
    if (userEmail) {
      subscribeUser(userEmail);
    }
  });

  $("#userEmail").on("change", (event) => {
    event.preventDefault();
    const email = event.target.value;
    validateEmail(email);
  });
})(jQuery);
