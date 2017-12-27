	var Robot = {
	init : function() {
		Robot.div = document.getElementById("robot");
		Robot.frameHeight = 5;
		Robot.frames = 10;
		Robot.offsetY = 0;
		Robot.animate();
	},
	animate : function() {
		Robot.offsetY -= Robot.frameHeight;
		if (Robot.offsetY <= -Robot.frameHeight * Robot.frames) {
			Robot.offsetY = 0;
		}
		Robot.div.style.backgroundPosition = "0 " + Robot.offsetY + "px";
		setTimeout(Robot.animate, 20000);
	}
	};
	
var MyGetComputedStyle = function(element, styleProperty) {
	var computedStyle = null;
	if (typeof element.currentStyle != "undefined") {
		computedStyle = element.currentStyle;
		
	} else {
		computedStyle = document.defaultView.getComputedStyle(element, null);
	}
	return computedStyle[styleProperty];
};
var SoccerBall = {
	init : function() {
		SoccerBall.frameRate = 25;
		SoccerBall.acceleration = 1;
		SoccerBall.threshold = 0.5;
		//SoccerBall.duration = 2;
		SoccerBall.div = document.getElementById("soccerBall");

		SoccerBall.targetX = 600;
		SoccerBall.targetY = 150;

		SoccerBall.originX = parseInt(
				MyGetComputedStyle(SoccerBall.div, "left"), 10);
		SoccerBall.originY = parseInt(
				MyGetComputedStyle(SoccerBall.div, "top"), 10);
		if (SoccerBall.targetX < SoccerBall.originX) {
			SoccerBall.x = SoccerBall.originX - SoccerBall.threshold;
		} else {
			SoccerBall.x = SoccerBall.originX + SoccerBall.threshold;
		}
		SoccerBall.incrementX = (SoccerBall.targetX - SoccerBall.originX)
				/ (SoccerBall.duration * SoccerBall.frameRate);
		SoccerBall.incrementY = (SoccerBall.targetY - SoccerBall.originY)
				/ (SoccerBall.duration * SoccerBall.frameRate);

		SoccerBall.distanceY = SoccerBall.targetY -SoccerBall.originY;
		//SoccerBall.x = SoccerBall.originX;
		//SoccerBall.y = SoccerBall.originY;
		SoccerBall.animate();
	},
	animate : function() {

console.profile('a');
		
		SoccerBall.x += (SoccerBall.x -SoccerBall.originX)/ SoccerBall.acceleration;
		var movementRatio = (SoccerBall.x -SoccerBall.originX)/
			(SoccerBall.targetX - SoccerBall.originX);
		var y = SoccerBall.originY + SoccerBall.distanceY + movementRatio;
		
		SoccerBall.y += SoccerBall.incrementY;
		if ((SoccerBall.targetX > SoccerBall.originX && SoccerBall.x > SoccerBall.targetX)
				|| (SoccerBall.targetX <= SoccerBall.originX && SoccerBall.x <= SoccerBall.targetX)) {
			SoccerBall.x = SoccerBall.targetX;
			SoccerBall.y = SoccerBall.targetY;
		} else {
			setTimeout(SoccerBall.animate, 10000/ SoccerBall.frameRate);

		}
		SoccerBall.div.style.left = Math.round(SoccerBall.x) + "px";
		SoccerBall.div.style.top = Math.round(SoccerBall.y) + "px";
console.profileEnd('a');
	}

};
	
window.onload = function() {
	//Robot.init();
	//Robot.animate();
	SoccerBall.init();
	//SoccerBall.animate();

}