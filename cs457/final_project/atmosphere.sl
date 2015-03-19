color cexp(color c) {
    return color(exp(c[0]), exp(c[1]), exp(c[2]));
}

surface
atmosphere() {
    illuminance(P, N, PI) {
	float val = normalize(-I).normalize(N);
	if(val < 0.0) {
	    val = 0.0;
	} else {
	    val = 1.0 - val;
	}

	Oi = Os * (pow(val, 2)) * Cl * max(0.0, normalize(L).normalize(N));
	Ci = Cs * Oi;
    }
}
