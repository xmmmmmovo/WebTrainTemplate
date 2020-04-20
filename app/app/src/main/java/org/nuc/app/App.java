package org.nuc.app;

import android.app.Application;

import org.nuc.app.config.InitConfig;

public class App extends Application {
    @Override
    public void onCreate() {
        super.onCreate();

        InitConfig.init(this)
                .withApiHost("http://127.0.0.1:9000/")
                .configure();
    }
}
