surface
planet_surf(
    float Ks = 0.9;
    float Kd = 0.5;
    float Ka = 0.0;
    float Roughness = 0.2;
    float DispAmp = 0.3;
    color SpecularColor = color(1, 1, 1);
) {
    // Generate some noise
    float magnitude = 0.;
    float size = 1.0;
    float i;
    for(i = 0.; i < 10.0; i += 1.0) {
	magnitude += (noise(size * P) - 0.5) / size;
	size *= 2.0;
    }

    float disp = magnitude * 0.3;
    color c;

    float spec = 0.0;
    if(disp > 0.09) {
	// Mountains
	c = color(1., 1., 1.);
	spec = 0.6;
    } else if(disp > 0.0) {
	// Land
	c = color(0.5, 0.9, 0.5);
	spec = 0.2;
    } else {
	// Water
	c = color(0.2, 0.2, 0.9);
	spec = 1.0;
    }


    // be sure the normal points correctly (used for lighting):
    varying vector Nf = faceforward(normalize(N), I);
    vector V = normalize(-I);

    illuminance(P, N, PI) {
	Ci = c * Ka * ambient();
	Ci = Ci + c	* Kd * diffuse(Nf);
	Ci = Ci + SpecularColor * Ks * specular(Nf, V, Roughness) * spec;

	// City lights
	if(disp > 0.0 && N.L < 0 && random() > 0.98) {
	    Oi = color(1.0);
	    Ci = color(1.0, 1.0, 1.0) * Oi;
	}
    }
}
