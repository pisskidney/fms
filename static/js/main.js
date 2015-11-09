$(function(){

    /* ------------------------ BUILD HOME ------------------------------*/
    $(document).ready(build_set_preview)

    function build_set_preview() {
        if (typeof(build_home_data) == 'undefined') {
            return
        }
        $('#build-theme-preview-header-wrapper').css(
            'background-image',
            'url(/static/' + build_home_data['bg']
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
        $('#id_bg').val($(this).attr('bgid'))
        // Mark as selected
        $('#build-theme-bg-images .selected').removeClass('selected')
        $(this).addClass('selected')
        // Chance preview image acordingly
        $('#build-theme-preview-header-wrapper').css(
            'background-image',
            'url(/static/' + $(this).attr('forpreview') + ')'
        );
    });
    /* -------------------------------------------------------------------*/

    var timer_check_domain;

    function set_check_domains_timer(site_name) {
        clearTimeout(timer_check_domain);
        timer_check_domain = setTimeout(
           check_domains,
           2000
        )
    }

    function check_domains() {
        // make ajax call and see if domains are free
        var site_name = $('#id_name').val();
        site_name = site_name.replace(/ /g, "");
        $.getJSON('/api/' + site_name, function(resp) {
            $('#build-name-img-inhouse-check').hide()
            $('#build-name-img-com-check').hide()
            if (resp['inhouse'] == true) {
                $('#build-name-img-inhouse-ok').show()
                $('#build-name-img-inhouse-bad').hide()
                $('#build-name-inhouse-status').html('available')
            } else {
                $('#build-name-img-inhouse-ok').hide()
                $('#build-name-img-inhouse-bad').show()
                $('#build-name-inhouse-status').html('taken')
            }
            if (resp['.com'] == true) {
                $('#build-name-img-com-ok').show()
                $('#build-name-img-com-bad').hide()
                $('#build-name-com-status').html('available')
            } else {
                $('#build-name-img-com-ok').hide()
                $('#build-name-img-com-bad').show()
                $('#build-name-com-status').html('taken')
            }
        });
    }

    $('#id_name').keyup(function() {
        var site_name = $('#id_name').val();
        site_name = site_name.replace(/ /g, "");
        if (site_name != "") {
            // set input values
            $('#build-name-domain-options').show();
            $('#id_name').val(site_name);
            $('.build-name-url b').html(site_name);
            // set gifs and disable buttons
            $('#build-name-img-inhouse-check').show()
            $('#build-name-img-inhouse-ok').hide()
            $('#build-name-img-inhouse-bad').hide()
            $('#build-name-inhouse-status').html('checking')

            $('#build-name-img-com-check').show()
            $('#build-name-img-com-ok').hide()
            $('#build-name-img-com-bad').hide()
            $('#build-name-com-status').html('checking')

            set_check_domains_timer(site_name)
        } else {
            $('#build-name-domain-options').hide();
        }
    });

});
