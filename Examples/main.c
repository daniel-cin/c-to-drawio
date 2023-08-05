potencia(float x, float y)
{
    float z;
    int p;
    if (y < 0)
    {
        p = 0 - y;
    }
    else
    {
        p = y;
    }
    z = 1.0;
    while (p != 0)
    {
        z = z * x;
        p = p - 1;
    }
    if (y < 0)
    {
        z = 1 / z;
    }
    print(z);
    return z;
}
