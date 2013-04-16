var Meal = Backbone.Model.extend({
	defaults: {
		"appetizer":  "caesar salad",
		"entree":     "ravioli",
		"dessert":    "cheesecake"
	}
	
});

__sort_by = function(type){
	return function(){
		this.models = _.sortBy(this.models, function(meal){
			return meal.attributes[type];
		})
		this.trigger("change");
	};
}

var Cookbook = Backbone.Collection.extend({

	model: Meal,

	url: '/meals/',

	save: function(){
		_.invoke(this.models,'save');
	},

	flip : function(){
		this.models.reverse();
		this.trigger("change");
	},

	sort_models_by_dessert: __sort_by('dessert'),

	sort_models_by_appetizer: __sort_by('appetizer'),

	sort_models_by_entree: __sort_by('entree')
});
