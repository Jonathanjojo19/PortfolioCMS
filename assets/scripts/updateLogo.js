function updateLogo(){
    event.preventDefault(true);
    let fields = document.forms["logo-form"].getElementsByTagName("input");
    let csrf_token_entry = fields[0].value;    
    let data = document.forms["logo-form"]["id_logo"].files[0];
    $.ajax({
        url: 'update-logo/',
        type: 'POST',
        cache: false,
        processData: false, 
        contentType: false,
        data: JSON.stringify({
            logo: data,
        }),
        beforeSend: function(request) {
            request.setRequestHeader('X-CSRFToken', csrf_token_entry);
        },
        success: function(result) {
            console.log(result);
            if (result.success){
                document.getElementById("update-status").innerText = result.message;
            } else {
                let errors = "";
                for (var key in result.message) {
                    result.message[key].forEach((er) => {
                        errors += er + "\n";
                    });
                }
                document.getElementById("update-status").innerText = errors;
            }
            $('#response-modal').modal('show');
        }
    });
}