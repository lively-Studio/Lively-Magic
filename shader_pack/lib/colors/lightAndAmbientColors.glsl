#ifndef INCLUDE_LIGHT_AND_AMBIENT_COLORS
    #define INCLUDE_LIGHT_AND_AMBIENT_COLORS

    #if defined OVERWORLD
        #ifndef COMPOSITE1
            vec3 noonClearLightColor = vec3(0.50, 0.40, 0.60) * 2.05; //ground and cloud color
        #else
            vec3 noonClearLightColor = vec3(0.30, 0.45, 0.80); //light shaft color
        #endif
        vec3 noonClearAmbientColor = pow(skyColor, vec3(0.75)) * 0.70;

        #ifndef COMPOSITE1
            vec3 sunsetClearLightColor = pow(vec3(0.55, 0.30, 0.45), vec3(1.5 + invNoonFactor)) * 5.0; //ground and cloud color
        #else
            vec3 sunsetClearLightColor = pow(vec3(0.50, 0.25, 0.40), vec3(1.5 + invNoonFactor)) * 6.8; //light shaft color
        #endif
        vec3 sunsetClearAmbientColor   = noonClearAmbientColor * vec3(0.90, 0.70, 1.10) * 0.85;

        #if !defined COMPOSITE1 && !defined DEFERRED1
            vec3 nightClearLightColor = 0.01 * vec3(0.01, 0.01, 0.02) * (0.4 + vsBrightness * 0.4); //ground color
        #elif defined DEFERRED1
            vec3 nightClearLightColor = 0.01 * vec3(0.01, 0.01, 0.02); //cloud color
        #else
            vec3 nightClearLightColor = 0.01 * vec3(0.01, 0.01, 0.02); //light shaft color
        #endif
        vec3 nightClearAmbientColor   = 0.01 * vec3(0.01, 0.01, 0.02) * (1.55 + vsBrightness * 0.77);

        #ifdef SPECIAL_BIOME_WEATHER
            vec3 drlcSnowM = inSnowy * vec3(-0.06, 0.0, 0.04);
            vec3 drlcDryM = inDry * vec3(0.01, -0.035, -0.06);
        #else
            vec3 drlcSnowM = vec3(0.0), drlcDryM = vec3(0.0);
        #endif
        #if RAIN_STYLE == 2
            vec3 drlcRainMP = vec3(-0.03, 0.0, 0.02);
            #ifdef SPECIAL_BIOME_WEATHER
                vec3 drlcRainM = inRainy * drlcRainMP;
            #else
                vec3 drlcRainM = drlcRainMP;
            #endif
        #else
            vec3 drlcRainM = vec3(0.0);
        #endif
        vec3 dayRainLightColor   = vec3(0.15, 0.10, 0.18) * 0.85 + noonFactor * vec3(0.0, 0.02, 0.06)
                                 + drlcRainM + drlcSnowM + drlcDryM;
        vec3 dayRainAmbientColor = vec3(0.15, 0.12, 0.25) * (1.8 + 0.5 * vsBrightness);

        vec3 nightRainLightColor   = 0.01 * vec3(0.01, 0.01, 0.02) * (0.5 + 0.5 * vsBrightness);
        vec3 nightRainAmbientColor = 0.01 * vec3(0.01, 0.01, 0.02) * (0.75 + 0.6 * vsBrightness);

        #ifndef COMPOSITE1
            float noonFactorDM = noonFactor; //ground and cloud factor
        #else
            float noonFactorDM = noonFactor * noonFactor; //light shaft factor
        #endif
        vec3 dayLightColor   = mix(sunsetClearLightColor, noonClearLightColor, noonFactorDM);
        vec3 dayAmbientColor = mix(sunsetClearAmbientColor, noonClearAmbientColor, noonFactorDM);

        vec3 clearLightColor   = mix(nightClearLightColor, dayLightColor, sunVisibility2);
        vec3 clearAmbientColor = mix(nightClearAmbientColor, dayAmbientColor, sunVisibility2);

        float rainShadowVisReduce = 0.0
            #ifdef SUN_MOON_DURING_RAIN
                #ifdef SPECIAL_BIOME_WEATHER
                    + 0.2 * inSnowy + 0.2 * inDry
                #elif RAIN_STYLE == 2
                    + 0.2
                #endif
            #else
                + 0.4
            #endif
        ;

        vec3 rainLightColor   = mix(nightRainLightColor, dayRainLightColor * (1.0 - rainShadowVisReduce), sunVisibility2) * 2.5;
        vec3 rainAmbientColor = mix(nightRainAmbientColor, dayRainAmbientColor * (1.0 + rainShadowVisReduce), sunVisibility2);

        vec3 lightColor   = mix(clearLightColor, rainLightColor, rainFactor);
        vec3 ambientColor = mix(clearAmbientColor, rainAmbientColor, rainFactor);
    #elif defined NETHER
        vec3 lightColor   = vec3(0.0);
        vec3 ambientColor = (netherColor + 0.5 * lavaLightColor) * (0.9 + 0.45 * vsBrightness);
    #elif defined END
        vec3 endLightColor = vec3(0.68, 0.51, 1.07);
        vec3 endOrangeCol = vec3(1.0, 0.3, 0.0);
        float endLightBalancer = 0.2 * vsBrightness;
        vec3 lightColor    = endLightColor * (0.35 - endLightBalancer);
        vec3 ambientColor  = endLightColor * (0.2 + endLightBalancer);
    #endif

#endif //INCLUDE_LIGHT_AND_AMBIENT_COLORS