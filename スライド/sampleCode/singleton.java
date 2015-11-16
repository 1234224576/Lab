public class MyClass{
	private static MyClass uniqueInstance;
	//他のプロパティ
	private MyClass(){} //コンストラクタをプライベートにし、MyClassだけがこれを呼び出せます！

	//getInstanceメソッドはこのクラスをインスタンス化し、そのインスタンスを返します
	public static MyClass getInstance(){
		if(uniqueInstance == null){
			uniqueInstance = new MyClass();
		}
		return uniqueInstance;
	}
	//他のメソッド
}