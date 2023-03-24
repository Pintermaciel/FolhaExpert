(function($) {
  "use strict"; // Start of use strict

  // Toggle the side navigation
  $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
    $("body").toggleClass("sidebar-toggled");
    $(".sidebar").toggleClass("toggled");
    if ($(".sidebar").hasClass("toggled")) {
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Close any open menu accordions when window is resized below 768px
  $(window).resize(function() {
    if ($(window).width() < 768) {
      $('.sidebar .collapse').collapse('hide');
    };
    
    // Toggle the side navigation when window is resized below 480px
    if ($(window).width() < 480 && !$(".sidebar").hasClass("toggled")) {
      $("body").addClass("sidebar-toggled");
      $(".sidebar").addClass("toggled");
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
  $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
    if ($(window).width() > 768) {
      var e0 = e.originalEvent,
        delta = e0.wheelDelta || -e0.detail;
      this.scrollTop += (delta < 0 ? 1 : -1) * 30;
      e.preventDefault();
    }
  });

  // Scroll to top button appear
  $(document).on('scroll', function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on('click', 'a.scroll-to-top', function(e) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    e.preventDefault();
  });

})(jQuery); // End of use strict

var options = {
  values: "a, b, c",
  ajax: {
    url: "ajax.php",
    type: "POST",
    dataType: "json",
    // Use "{{{q}}}" as a placeholder and Ajax Bootstrap Select will
    // automatically replace it with the value of the search query.
    data: {
      q: "{{{q}}}"
    }
  },
  locale: {
    emptyTitle: "Select and Begin Typing"
  },
  log: 3,
  preprocessData: function(data) {
    var i,
      l = data.length,
      array = [];
    if (l) {
      for (i = 0; i < l; i++) {
        array.push(
          $.extend(true, data[i], {
            text: data[i].Name,
            value: data[i].Email,
            data: {
              subtext: data[i].Email
            }
          })
        );
      }
    }
    // You must always return a valid array when processing data. The
    // data argument passed is a clone and cannot be modified directly.
    return array;
  }
};

$(".selectpicker")
  .selectpicker()
  .filter(".with-ajax")
  .ajaxSelectPicker(options);
$("select").trigger("change");

function chooseSelectpicker(index, selectpicker) {
  $(selectpicker).val(index);
  $(selectpicker).selectpicker('refresh');
}