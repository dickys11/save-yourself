package com.example.saveyourself

class MainActivity : androidx.appcompat.app.AppCompatActivity() {

    private val client = okhttp3.OkHttpClient()

    override fun onCreate(savedInstanceState: android.os.Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        run("http://34.87.19.67:8888/getstatus/(username)/(numpage)")
    }

    private fun run(block: String) {

    }
}
