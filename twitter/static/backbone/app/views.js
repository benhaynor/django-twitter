$$ = $;

var MealView = Backbone.View.extend({
	tagName:  "div",
	className: "meal",
	initialize : function(){
		this.listenTo(this.model, "change", this.render);
		this.template = $$("#mealTemplate").html();
		this.render();
	},

	render : function(){
		var html = Mustache.render(this.template,this.model.attributes);
		this.$el.html(html);
		return this;
	}
});

var CookbookView = Backbone.View.extend({

	initialize : function() {
		this.listenTo(this.collection, "change", this.render);
		this.listenTo(this.collection, "reset", this.render);
		this.template = $$("#mealTemplate").html();
	},
	
	render: function() {
		var mealViews = _.map(this.collection.models, function(model){
			return new MealView({model: model});
		});
		this.$el.empty();
		this.$el.append(_.map(mealViews,function(view){
			return view.$el;
		}));
	}
});

var AddMealView = Backbone.View.extend({

	el: '#create-meal',
	
   	events : {
        "click button" :"changed"
    },

	changed:function(evt) {
		var new_meal_hash = _.object(
			this.$el.serializeArray().map(
				function(object){
					return [object.name, object.value]
				})
			);	
		var new_meal = new Meal(new_meal_hash);
		cookbook.add(new_meal);
		cookbook.trigger("change");
	}
});

var SortMealView = Backbone.View.extend({

	el: '#meal-ordering',

	events : {
		"click" :"changeOrder"
	},
	
	changeOrder: function(ent){
		window.console.log('ckicked me');
		var sort_order_choice = $('input:radio[name=order]:checked').val();
		window.console.log(sort_order_choice);
		cookbook['sort_models_by_' + sort_order_choice]();
	}
	
});
