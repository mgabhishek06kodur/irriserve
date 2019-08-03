package com.example.lenovo.irriserve;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class dashboard extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);
    }



    public void soil_moisture(View view) {
        Intent i1=new Intent(this,soil_moisture.class);
        startActivity(i1);
    }
    public void humidity(View view) {
        Intent i2=new Intent(this,humidity.class);
        startActivity(i2);
    }
    public void temperature(View view) {
        Intent i3=new Intent(this,temperature.class);
        startActivity(i3);
    }
    public void doMore(View view) {
        Intent i4=new Intent(this,weblue.class);
        startActivity(i4);
    }
}
