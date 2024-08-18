$("#image-form").submit(function (e) {
    e.preventDefault();

    // Check if image was provided
    if(!$("#image").val()) {
        alert("Please select an image to upload!");
        return;
    }

    // Hide content on page
    $("#main").hide();

    // Show loading circle
    $("#loader").show();

    var formData = new FormData(this);

    // Perform POST request to send image
    $.ajax({
        url: "",
        type: "POST",
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            // Hide loading circle
            $("#loader").hide();

            // Show content on page
            $("#main").show();

            // Display image
            var img_base64 = response.image;
            var img = document.createElement("img");
            img.class = "img-fluid";
            img.style.width = "100%";
            img.src = "data:image/jpeg;base64," + img_base64;
            
            // Add image to screen
            $("#image-container").html(img);

            $("#download-btn").attr("download", "results.jpeg");
            $("#download-btn").attr("target", "_blank");
            $("#download-btn").attr("href", "data:image/jpeg;base64," + img_base64);

            $("#imageModal").modal('show');
        },
        error: function (xhr, textStatus, error) {
            // Handle error response
        },
    });
});

$("#new-face-form").submit(function (e) { 
    e.preventDefault();

    console.log("Submit");

    // TODO: Check if image was provided

    // Hide content on page
    $("#new-face-modal .btn-close").click()
    $("#main").hide();

    // Show loading circle
    $("#loader").show();

    var formData = new FormData(this);

    // Perform POST request to create new person
    $.ajax({
        url: "/faces/",
        type: "POST",
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            location.reload();
        },
        error: function (xhr, textStatus, error) {
            // Handle error response
        },
    });
});