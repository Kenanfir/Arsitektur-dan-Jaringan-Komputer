#include <iostream>             // user-defined iostream
#include <thread>               // user-defined thread
#include <mutex>                // user-defined mutex
#include <condition_variable>   // user-defined mutex

using namespace std::literals::chrono_literals; // Untuk memberi delay pada thread

std::mutex m;               // Deklarasi data mutex untuk mengunci dan membuka objek program
std::condition_variable c;  // Deklarasi data condition yang bisa dibagikan pada thread lain
int number = 1, max;        // Deklarasi data integer

void PrintOdd() // Fungsi thread print pada bilangan ganjil
{
    for (; number < max;)   // Loop yang dijalankan hingga jumlah number sama dengan max
    {
        std::unique_lock<std::mutex> lock(m);               // Memberi data unik agar bisa akses condition_variable
        c.wait(lock, []() { return (number % 2 == 1); });   // Kondisi mengambil number pada saat ganjil dan mengunci objek program
        std::cout << number << std::endl;                   // Program print data pada number
        std::this_thread::sleep_for(1s);                    // Delay pada function
        number++;                                           // Number ditambah satu
        lock.unlock();                                      // Membuka kuncian objek program
        c.notify_all();                                     // Notify kondisi mutex pada function thread even
    }

}

void PrintEven()    // Fungsi thread print pada bilangan genap
{
    for (; number < max;)    // Loop yang dijalankan hingga jumlah number sama dengan max
    {
        std::unique_lock<std::mutex> lock(m);               // Memberi data unik agar bisa akses condition_variable
        c.wait(lock, []() { return ( number % 2 == 0); });  // Kondisi mengambil number pada saat genap dan mengunci objek program
        std::cout << number << std::endl;                   // Program print data pada number
        std::this_thread::sleep_for(2.5s);                  // Delay pada function
        number++;                                           // Number ditambah satu
        lock.unlock();                                      // Membuka kuncian objek program
        c.notify_all();                                     // Notify kondisi mutex pada function thread ganjil
    }
}

int main()  // Main function program
{
    std::cout << "Set Max Number \n";   // Program print untuk meminta data max
    std::cin >> max;                    // Program memasukan data yang telah diketik user

    std::thread OddThread(PrintOdd);    // Deklarasi thread ganjil dengan funsi PrintOdd
    std::thread EvenThread(PrintEven);  // Deklarasi thread genap dengan funsi PrintEven
    OddThread.join();                   // Thread akan jalan hingga fungsi PrintOdd selesai
    EvenThread.join();                  // Thread akan jalan hingga fungsi PrintEven selesai
    return 0;                           // Return program menjadi seperti awal
}