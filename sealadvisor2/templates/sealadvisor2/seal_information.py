
{% extends 'sealadvisor2/base.html' %}
{% load static %}
{% load material_form %} 			

{% block content %}
<h1>Supreme Sealadvisor</h1>
<a class='wave-effect btn orange' href="{% url 'sealadvisor2:index' %}">Back to overview</a>
<a class='wave-effect btn orange' href="{% url 'sealadvisor2:supreme' %}">Add new supreme advise</a>
<div class='row'>
	<div class='col s6'>
		<div class='card teal lighten-4'>
			<div class='card-content'>
				<span class='card-title black-text'>Supreme</span>
				<form method="POST" class="post-form">
                    {% csrf_token %}
                    {% form form=form %} {% endform %}

                    <br>
                    <button type="submit" class="save btn btn-default">Save</button>
                    <a class='wave-effect btn' href="{% url 'sealadvisor2:index' %}">Cancel</a>
                </form>
			</div>
		</div>
	</div>
	<div class='col s6'>
		<div class='card teal lighten-4'>
            <div class='card-content'>
                <span class='card-title black-text'>Next steps</span>
                {% if advise.fwd_seal %}
                <p><a class='wave-effect btn' href="{% url 'sealadvisor2:supremeFwd' advise.id %}">Add forward seal information</a></p>
                {% endif %}
                <p><a class='wave-effect btn' href="{% url 'sealadvisor2:index' %}">Add aft seal information</a></p>
                <p><a class='wave-effect btn' href="{% url 'sealadvisor2:index' %}">Add environmental information</a></p>
            </div>
        </div>
	</div>

</div>

<script type='text/javascript'>
(function($) {
    $(function() {
        var selectField = $('#id_application');
        var fwd = $('#id_fwd_seal');
        var aft = $('#id_aft_seal');

        function toggleVerified(value) {
            value == '1' ? fwd.parent().show() : fwd.parent().hide();
            value == '1' ? aft.parent().show() : aft.parent().hide();
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(jQuery);

</script>

{% endblock %}	 