package org.nuc.app.config;

import java.util.WeakHashMap;

public class Configurator {
    private static final WeakHashMap<String, Object> CONFIGS = new WeakHashMap<>();

    private Configurator() {
        CONFIGS.put(ConfigKeys.CONFIG_READY.name(), false);

    }

    public static class Holder{
        private static final Configurator INSTANCE = new Configurator();
    }

    public final WeakHashMap<String, Object> getConfigs() {
        return CONFIGS;
    }

    public static Configurator getInstance() {
        return Holder.INSTANCE;
    }

    public final void configure() {
        CONFIGS.put(ConfigKeys.CONFIG_READY.name(), true);
    }

    public final Configurator withApiHost(String host) {
        CONFIGS.put(ConfigKeys.API_HOST.name(), host);
        return this;
    }

    private void checkConfiguration() {
        if (!(boolean)CONFIGS.get(ConfigKeys.CONFIG_READY.name())){
            throw new RuntimeException("配置未完成");
        }
    }

    public <T> T getConfiguration(Enum<ConfigKeys> key) {
        checkConfiguration();
        return (T) CONFIGS.get(key.name());
    }
}
