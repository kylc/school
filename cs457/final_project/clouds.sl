surface
clouds(
    float Kd = 1.0;
) {
    // Generate some noise
    float magnitude = 0.;
    float size = 1.0;
    float i;
    for(i = 0.; i < 10.0; i += 1.0) {
	magnitude += (noise(size * P) - 0.5) / size;
	size *= 2.0;
    }

    // Be sure the normal points correctly (used for lighting)
    varying vector Nf = faceforward(normalize(N), I);
    vector V = normalize(-I);

    // Calculate the color
    illuminance(P, N, PI) {
	// Only draw clouds on the lit side of the planet
	if(magnitude > 0.1 && N.L > 0.0) {
	    N = N + normalize(N) * magnitude;
	    Ci = Cs * Kd * diffuse(Nf);
	} else {
	    Oi = color(0.0);
	    Ci = Cs * Oi;
	}
    }
}
