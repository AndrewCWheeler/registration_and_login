$().ready(function() {
    $('#register').validate({
        
        rules: {
            first_name: {
                required: true, 
                minlength: 2
            },
            last_name: {
                required: true, 
                minlength: 2
            },
            email: {
                required: true, 
                email: true
            },
            password: {
                required: true, 
                minlength: 8
            },
            confirm_password: {
                required: true, 
                minlength: 8, 
                equalTo: '#password'
            },
        },
        messages: {
            first_name: {
                required: "Please enter your first name",
                minlength: "Must be more than 2 characters"
            },
            last_name: {
                required: "Please enter your last name",
                minlength: "Must be more than 2 characters"
            },
            password: {
                required: "Please provide a password", 
                minlength: "Your password must be at least 8 characters long"
            },
            confirm_password: {
                required: "Please provide a matching password", 
                minlength: "Your password must be at least 8 characters long",
                equalTo: "Your passwords do not match"
            },
        }
    })

    $('#login').validate({
        rules: {
            email: {
                required: true, 
                email: true
            },
            password: {
                required: true, 
                minlength: 8
            },
        },
        messages: {
            password: {
                required: "Please enter your password", 
                minlength: "Password must be at least 8 characters long"
            }
        }
    })
});