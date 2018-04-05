// def main(args):
//     ileKw = int(input("Podaj ilość losowanych punktów: "))
//     ileKo = 0
//     r = 1

//     for i in range(ileKw):
//         x = random.random()
//         y = random.random()
//         if x**2 + y**2 <= r**2:
//             ileKo += 1

//     pi = 4 * ileKo / ileKw
//     print("Przybliżona wartość pi: ", pi)

szerokosc = 640;
wysokosc = 480;

ileKw = prompt("Podaj ilość punktów: ", 100);
ileKo = parseInt(ileKw);
r = prompt("Podaj promień: ", 100);
ileKo = 0;

function getRnd(min, max) {
	return Math.random() * (max - min) + min;
}

lx = [];
ly = [];

for (i = 0; i < ileKw; i++) {
	x = Math.floor(getRnd(r, -r));
	y = Math.floor(getRnd(r, -r));
	// console.log(x);
	// console.log(y);
	lx[i] = x;
	lx[i] = y;
	if (x*x + y*y <= r*r) {
		ileKo++;
	}
}

console.log(x);
pi = 4 * ileKo / ileKw;
alert("Przybliżona wartość pi: " + pi);

function setup() {
  createCanvas(szerokosc, wysokosc);
  stroke('#666');
  background('#00ff00');
  ellipse(szerokosc / 2, wysokosc / 2, 2 * r, 2 * r);
  line(szerokosc / 2, szerokosc / 2, wysokosc);
  line(0, wysokosc / 2, szerokosc, wysokosc / 2);
}

x_offset = szerokosc / 2;
y_offset = wysokosc / 2;


function draw() {
	for (i = 0; i < ileKw; i++) {
		if (lx[i]*lx[i] + ly[i]*ly[i] <= r*r) {
			stroke('#f00');
		} else {
				stroke('#000');
		}
		point(lx[i] , ly[i]);
	}
}