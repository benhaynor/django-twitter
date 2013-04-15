$(function(){
/*meal1 = new Meal({
	"appetizer":  "a",
    "entree":     "b",
    "dessert":    "d"
});
meal2 = new Meal({
	"appetizer":  "d",
    "entree":     "b",
    "dessert":    "a"
});
meal3 = new Meal({
	"appetizer":  "c",
    "entree":     "c",
    "dessert":    "c"
});

meals = [meal1,meal2,meal3];
mealViews = _.map(meals,function(meal){
	return new MealView({model: meal});
});
cookbook = new Cookbook(meals); 
cookbookView = new CookbookView({collection: cookbook});
cookbookView.render();
$("#content").append(cookbookView.$el);*/
cookbook = new Cookbook();
cookbookView = new CookbookView({collection: cookbook});
cookbookView.render();
addMealView = new AddMealView();
sortMealView = new SortMealView;
cookbook.fetch();
$("#content").append(cookbookView.$el);
});
