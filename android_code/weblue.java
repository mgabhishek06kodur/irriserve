package com.example.lenovo.irriserve;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class weblue extends AppCompatActivity {
    Button button1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_weblue);
        button1 = (Button) findViewById(R.id.b1);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i3 = getPackageManager().getLaunchIntentForPackage("project.bluetoothterminal");
                startActivity(i3);
            }
        });
    }


    public void hello(View view) {
           switch (view.getId()){
               case R.id.b2:
                   Intent i4=new Intent(Intent.ACTION_VIEW,Uri.parse("http://infobeginner.tech/"));
                   startActivity(i4);
                   break;
               case R.id.b3:
                   Intent i5=new Intent(Intent.ACTION_DIAL,Uri.parse("tel:9964000846"));
                   startActivity(i5);
                   break;


           }
    }
}
