$(document).ready(function() {
    $("#tester-box").bind('keypress keyup blur', function() {
        if ($(this).val() == '') {
            $(".sample").text('Jove xef, porti whisky amb quinze glaçons d\'hidrogen, coi!');       
        }
        else {
            $(".sample").text($(this).val());
        } 
    });

/* Placeholder for text inputs */
  if(!Modernizr.input.placeholder){

      $('[placeholder]').focus(function() {
        var input = $(this);
        if (input.val() == input.attr('placeholder')) {
          input.val('');
          input.removeClass('placeholder');
        }
      }).blur(function() {
        var input = $(this);
        if (input.val() == '' || input.val() == input.attr('placeholder')) {
          input.addClass('placeholder');
          input.val(input.attr('placeholder'));
        }
      }).blur();
      $('[placeholder]').parents('form').submit(function() {
        $(this).find('[placeholder]').each(function() {
          var input = $(this);
          if (input.val() == input.attr('placeholder')) {
            input.val('');
          }
        })
      });
  }
  
});
