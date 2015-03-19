displacement
planet_disp(
    float DispAmp = 0.15;
) {
    // Generate some noise
    float magnitude = 0.;
    float size = 1.0;
    float i;
    for(i = 0.; i < 10.0; i += 1.0) {
	magnitude += (noise(size * P) - 0.5) / size;
	size *= 2.0;
    }

    float disp = magnitude * DispAmp;

    if(disp < 0.) {
	// Water has much less variance than land
	disp *= 0.1;
    }

    if(disp != 0.) {
	normal n = normalize(N);

	// Actual displacement
	P = P + disp * n;
	N = calculatenormal(P);

	// Bump mapping
	// N = calculatenormal(P + disp * n);
    }
}
