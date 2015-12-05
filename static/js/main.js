$(function(){

    /* ------------------------ BUILD HOME ------------------------------*/
    $(document).ready(build_set_preview)
    $(document).ready(build_button_types)
    $(document).ready(set_default_button_type)

    function apply_css(select, css_arr) {
        for (j=0; j<css_arr.length; j++) {
            csskey = css_arr[j][0]
            cssval = css_arr[j][1]
            // replace {{colorx}} with proper colors
            for (k=1; k<=5; k++)
                cssval = cssval.replace('{{color'+k+'}}', build_home_data['color'+k])      
            $(select).css(csskey, cssval)
        }
    }

    function set_default_button_type() {
        //@TODO better js granularization. check what page it is
        $('#id_header_button').val($('#build-home-buttons .selected').attr('forbutt'))
    }

    function build_button_types() {
        if (typeof(build_button_data) == 'undefined' || typeof(build_home_data) == 'udnefined') {
            return
        }
        // Set css on buttons 
        data = build_button_data
        for (i=0; i<data.length; i++) {
            select = '#build-home-buttons .button-type-' + data[i]['id']
            apply_css(select, data[i]['css'])
        }
    }

    function build_set_preview() {
        if (typeof(build_home_data) == 'undefined') {
            return
        }
        $('#build-theme-preview-header-wrapper').css(
            'background-image',
            'url(/static/' + build_home_data['bg'] + ')'
        )
        $('#build-theme-preview-nav').css(
            'background-color',
            build_home_data['color1']
        )
        $('#build-theme-preview-header-button').css(
            'background-color',
            build_home_data['color2']
        )
        $('#build-theme-preview-nav').css(
            'color',
            build_home_data['color3']
        )
        $('#build-theme-preview-header-button').css(
            'color',
            build_home_data['color3']
        )
    }

    $('#form-build-home #id_title').keyup(function() {
        updated_title = $('#form-build-home #id_title').val()
        $('#build-theme-preview-header-title').html(updated_title)
    })

    $('#form-build-home #id_motto').keyup(function() {
        updated_motto = $('#form-build-home #id_motto').val()
        $('#build-theme-preview-header-subtitle').html(updated_motto)
    })

    $('#build-home-buttons li').click(function() {
        // Set form value
        $('#id_header_button').val($(this).attr('forbutt'))
        // Mark as selected
        $('#build-home-buttons .selected').removeClass('selected')
        $(this).addClass('selected')
        // Update preview
        for (i=0; i<build_button_data.length; i++) {
            if (build_button_data[i]['id'] == $(this).attr('forbutt')) {
                apply_css('#build-theme-preview-header-button', build_button_data[i]['css'])
                break
            }
        }
    })
    
    /* ------------------------ BUILD THEME ------------------------------*/
    $(document).ready(build_theme_set_preview)

    function build_theme_set_preview() {
        $('#build-theme-bg-images .selected').trigger('click')
        $('#build-theme-colors .selected').trigger('click')
    }

    $('#build-theme-colors li').click(function() {
        // Mark selected
        $('#build-theme-colors .selected').removeClass('selected')
        $(this).addClass('selected')
        // Set form value
        $('#id_theme').val($(this).attr('themeid'))
        // Change preview div
        $(this).children('div').children('span').each(function (i) {
            color = $(this).attr('color')
            if (i == 0) {
                // Navbar bg color
                $('#build-theme-preview-nav').css(
                    'background-color',
                    color
                )
            }
            else if (i == 1) {
                // Button color
                $('#build-theme-preview-header-button').css(
                    'background-color',
                    color
                )
            }
            else if (i == 2) {
                // Navbar text color
                $('#build-theme-preview-nav').css(
                    'color',
                    color
                )
                // button text color
                $('#build-theme-preview-header-button').css(
                    'color',
                    color
                )
            }
            else if (i == 3) {

            }
            else if (i == 4) {

            }
        });
    });

    $('#build-theme-bg-topics li').click(function() {
        if (!$(this).hasClass('active')) {
            // Get the currently shown div class (class = topic id; linked)
            old_div_class = '.' + $('#build-theme-bg-topics .active').attr('id')
            // Change toggle correct topic
            $('#build-theme-bg-topics .active').removeClass('active')
            $(this).addClass('active')
            // Toggle div corresponding to clicked topic
            $('.' + $(this).attr('id')).toggle()
            $(old_div_class).toggle()
        }
    });

    $('#build-theme-bg-images li').click(function() {
        // Set form value
        $('#form-build-theme #id_bg').val($(this).attr('bgid'))
        // Mark as selected
        $('#build-theme-bg-images .selected').removeClass('selected')
        $(this).addClass('selected')
        // Chance preview image acordingly
        $('#build-theme-preview-header-wrapper').css(
            'background-image',
            'url(/static/' + $(this).attr('forpreview') + ')'
        );
    });
    /* ------------------------- BUILD NAME ---------------------------*/

    var timer_check_domain;

    function set_check_domains_timer(site_name) {
        clearTimeout(timer_check_domain);
        timer_check_domain = setTimeout(
           check_domains,
           1000
        )
    }

    $('#build-name-input').keyup(function() {
        $('#id_name').val($(this).val())
    });

    function check_domains() {
        // make ajax call and see if domains are free
        var site_name = $('#build-name-input').val();
        site_name = site_name.replace(/ /g, "");
        $.getJSON('/api/' + site_name, function(resp) {
            $('#build-name-img-subdomain-check').hide()
            $('#build-name-img-com-check').hide()

            if (resp['subdomain'] == true) {
                $('#build-name-img-subdomain-ok').show()
                $('#build-name-img-subdomain-ok').hide()
                $('#build-name-butt-subdomain').show()
                $('#build-name-img-subdomain-bad').hide()
            } else {
                $('#build-name-img-subdomain-ok').hide()
                $('#build-name-img-subdomain-bad').show()
            }
            if (resp[site_name+'.com'] == true) {
                $('#build-name-img-com-ok').show()
                $('#build-name-img-com-bad').hide()
                $('#build-name-img-com-ok').hide()
                $('#build-name-butt-com').show()
            } else {
                $('#build-name-img-com-ok').hide()
                $('#build-name-img-com-bad').show()
            }
        });
    }

    $('#build-name-input').keyup(function() {
        var site_name = $('#build-name-input').val();
        site_name = site_name.replace(/ /g, "");
        if (site_name != "") {
            // set input values
            $('.build-name-options-data').show()
            $('.build-name-options-description').hide()
            $('.build-name-url b').html(site_name);
            $(this).val(site_name)
            // set gifs and disable buttons
            $('#id_name').val(site_name);

            $('#build-name-butt-subdomain').hide()
            $('#build-name-butt-com').hide()

            $('#build-name-img-subdomain-check').show()
            $('#build-name-img-subdomain-ok').hide()
            $('#build-name-img-subdomain-bad').hide()

            $('#build-name-img-com-check').show()
            $('#build-name-img-com-ok').hide()
            $('#build-name-img-com-bad').hide()

            set_check_domains_timer(site_name)
        } else {
            $('.build-name-options-data').hide();
            $('.build-name-options-description').show();
        }
    });

});
