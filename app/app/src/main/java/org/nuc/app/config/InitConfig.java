package org.nuc.app.config;

import android.content.Context;

import java.util.WeakHashMap;

public class InitConfig {
    public static Configurator init(Context context) {
        getConfigurations().put(ConfigKeys.APPLICATION_CONTEXT.name(), context.getApplicationContext());
        return Configurator.getInstance();
    }

    public static WeakHashMap<String, Object> getConfigurations() {
        return Configurator.getInstance().getConfigs();
    }
}
