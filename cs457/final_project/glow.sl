surface
glow() {
    float dist = (distance(point(P[0], P[1], 0), point(0, 0, 0))) - 4.5;

    Oi = Os * abs(1.0 / dist);
    Ci = Oi * Cs;
}
